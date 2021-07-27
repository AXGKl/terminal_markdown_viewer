#!/usr/bin/bash

TERMINAL="${TERMINAL:-st}"

here="$(dirname "$0")"
cd "$here"

funcs() {
    local a="func"
    grep "${a}tion" ./make | grep " {" | sed -e "s/${a}tion/- /g" | sed -e 's/{//g' | sort
}

doc="
# Repo Maintenance Functions

## Usage: ./make <function> [args]

## Functions:
$(funcs)
"

sh() {
    echo -e "Running: \x1b[32m$*\x1b[0m"
    eval "$@"
}

exit_help() {
    echo -e "$doc"
    exit 1
}
function test {
    pytest -xs tests
}
function docs_regen {
    run doc pre_process
    pre_process \
        --patch_mkdocs_filewatch_ign_lp \
        --gen_theme_link \
        --gen_last_modify_date \
        --gen_change_log \
        --gen_credits_page \
        --gen_auto_docs \
        --lit_prog_evaluation=md \
        --lit_prog_evaluation_timeout=5 \
        --lit_prog_on_err_keep_running=false

}
function docs {
    sh docs_regen
    sh mkdocs build
}

function docs_serve {
    # `doc pp -h` reg. what this does:
    sh doc pre_process --lpem=true --lpe=md
}

ds() { docs_serve "$@"; }

main() {
    test -z "$1" && exit_help
    test "$1" == "-h" && exit_help
    func="$1"
    shift
    $func "$@"
}

main "$@"
