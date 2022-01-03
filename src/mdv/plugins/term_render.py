from mdv import tools
from mdv.plugs import plugins

plugin = 'renderer'

block = b'\x01'
ignore = {'style', 'br'}


class Block:
    """Represents a matrix of cells, corresponding to a display=block tag
    cells *before* layout is like:
        [[('foo', tag.ns), ('bar', tag.ns)],  # line1
         [('foo', tag.ns), ('bar', tag.ns)],  # line2
          innerblock,                         # many lines
          [..<further inline text tuples>]]

    """

    width = height = 0

    def __init__(self, tag):
        self.tag = tag
        self.name = tag.name
        self.cells = []
        self.rendered_cells = []
        self.blocks = {}
        self.rendered = False
        self.height = self.width = 0

    def new_line(self):
        l = []
        self.cells.append(l)
        return l

    def embed(self, block, at):
        """nests an inner block into us - at the left top cell
        """

    def render(self):
        """After this our cells contain the rendered lines of the border box
        We have no nested blocks within us (going inside to out)"""
        tag = self.tag
        s = self.tag.style
        lbl, lbr, bt, bl, br, bb = s.rendered_border
        pl, pr = s.padding_left, s.padding_right
        padding_box_width = s.content_width + pl + pr
        if bt:
            # border top:
            r = bt(padding_box_width)
        else:
            r = []
        pl, pr = ' ' * pl, ' ' * pr
        w = s.content_width
        pt = s.padding_top
        pb = s.padding_bottom
        if pt or pb:
            t = pl + w * ' ' + pr
        if pt:
            r.extend([bl + s.format_txt(t) + br for i in range(pt)])
        self.left_bp, self.right_bp = bl + s.format_txt(pl), s.format_txt(pr) + br
        marg_collapse = 0
        for row in self.cells:
            if not row:
                continue
            if isinstance(row[0], Block):
                b = row[0]
                b.y0 = len(r)  # row index where this block must be inserted
                self.blocks.setdefault(b.y0, []).append(b)
                marg_collapse = self.embed_block(b, into=r, collapse=marg_collapse)
                # b.x0, b.y0 = (b.tag.style.margin_left,)
                # [r.append(self.left_bp + l + self.right_bp) for l in b.cells]
            else:
                marg_collapse = 0
                line = self.left_bp
                for cell in row:
                    txt, style = cell
                    line += style.format_txt(txt)
                line += self.right_bp
                r.append(line)
        if pb:
            r.extend([bl + s.format_txt(t) + br for i in range(pb)])
        if bb:
            r.extend(bb(padding_box_width))
        # self.embed_blocks(into=r)

        self.height = len(r)
        self.width = s.outer_width - s.margin_left - s.margin_right
        self.rendered_cells = r
        self.rendered = True
        return r

    def embed_block(self, block, into, collapse):
        """collapse: # https://www.w3schools.com/css/css_margin_collapse.asp
        """
        s = self.tag.style
        bs = block.tag.style
        mt, mb = bs.margin_top, bs.margin_bottom
        mt = max(0, mt - collapse)
        if mt or mb:
            l = s.format_txt(' ' * block.width)
            tm = [l for i in range(mt)]
            tb = [l for i in range(mb)]
            lines = tm + block.rendered_cells + tb
        else:
            lines = block.rendered_cells
        for line in lines:
            l = self.left_bp + s.format_txt(' ' * bs.margin_left) + line
            l += s.format_txt(' ' * bs.margin_right) + self.right_bp
            into.append(l)
        return mb

    def __repr__(self):
        k = ['%s (%sx%s)' % (self.tag.name, self.height, self.width), tools.ruler()]
        if not self.rendered:
            return str(k)
        k.extend(self.rendered_cells)
        return '\n'.join(k)


def make_block(tag):
    w = tag.style.content_width
    # will recurse back into this make_block, at block tags
    block = Block(tag)
    make_inline_blocks(tag, block, w, w, fill=None)
    block.render()
    return block


def visualize(tag):
    return make_block(tag).rendered_cells


class PseudoTag:
    def __init__(self, tag):
        self.name = n = tag.name + ':before'
        self.parent = tag
        self.style = plugins.style.Style(self, n)
        self.style._.update(tag.style._['before'])
        self.style._['display'] = 'inline'

    def __iter__(self):
        yield ''  # text is within content, which is evaled in text_pre


def make_before_pseudo_tag(tag):
    pt = PseudoTag(tag)
    return pt
    # have to fulfil bs4 api


def make_inline_blocks(outer_tag, block, width, rest, fill):
    """
    tag: inline or block
    block: the current holding display=block

    fill: Either None, then we make a new line or the end of a current line, then we fill it up
    (fill is the current (last) line of the outer_block)

    Recursion below:
        - we might stumble over nested display=blocks
        - Also we have <em><strong>... i.e. nested inlines
    """
    l = block.new_line() if fill is None else fill
    for tag in outer_tag:
        # print('tag', tag.name or 'str', str(tag))
        # bs4 already navigable string (the leafs(text) within a tag)?
        if not isinstance(tag, str):

            if tag.style.display == 'block':
                # an inner block within block - first fill the current line:
                if l and l[-1] and rest < width:
                    l.append(fill_line(rest, outer_tag.style))

                if tag.name in ignore:
                    pass
                else:
                    b = make_block(tag)
                    l.append(b)
                rest = width
                l = block.new_line()
                continue
            else:
                rest = make_inline_blocks(tag, block, width, rest, fill=l)
                # inline writing may have added new lines:
                l = block.cells[-1]
        else:
            if outer_tag.style._.get('before'):
                t = make_before_pseudo_tag(outer_tag)
                rest = make_inline_blocks(t, block, width, rest, fill=l)
                l = block.cells[-1]

            # tag is here the navigable string of bs4:
            style = outer_tag.style
            # text pre returns a function of actual text str -> we can copy tags for
            # others
            t = style.text_pre_wrap(str(tag))
            while t:
                if rest == width:
                    t = t.lstrip()
                    if not t:
                        break
                s = t
                # if s and not l:
                #     l = block.new_line()
                rest = rest - len(s)
                if rest < 0:
                    s, r, t = fit_into_line(t, rest + len(s), width)
                    if s:
                        l.append(col(s, style))
                    if r:
                        st = block.tag.style if not s else outer_tag.style
                        l.append(fill_line(r, st))
                    l = block.new_line()
                    rest = width
                    continue

                if rest > 0:
                    l.append(col(s, style))

                elif rest == 0:
                    l.append(col(s, style))
                    l = block.new_line()
                    rest = width
                break

    if rest and rest < width and l and outer_tag == block.tag:
        l.append(fill_line(rest, outer_tag.style))
        rest = width
    # if l[-1] == '':
    #    l.pop()
    return rest


col = lambda s, item: (s, item)


def fit_into_line(s, rest, width):
    """
    Known:
    - item.t is longer than rest
    - rest > 0
    """
    assert len(s) > rest and rest > 0 and width > 0
    ss = s[:rest]
    # word break fits?
    if s[rest] == ' ':
        return ss, 0, s[rest:]
    ssw = ss.rsplit(' ', 1)[0]
    # no space at first char:
    if ssw and len(ssw) < rest:
        # fits?
        return ssw, rest - len(ssw), s[len(ssw) :]
    if rest == width:
        # full line avail, nothing fits -> break word
        return ss, 0, s[rest:]

    # partial line -> fill it up:
    return '', rest, s


def fill_line(chars, tag):
    return col(' ' * chars, tag)
