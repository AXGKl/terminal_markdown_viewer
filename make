#!/usr/bin/env bash
# Lacking proper Makefile skills

set -e

TERMINAL="${TERMINAL:-st}"

here="$(dirname "$0")"
cd "$here"

funcs() {
    local a="func"
    grep "${a}tion" ./make | grep " {" | sed -e "s/${a}tion/- /g" | sed -e 's/{//g' | sort
}
aliases() {
    set -x
    local a="## Function"
    set +x
    grep -A 30 "$a Aliases:" ./make | grep -B 30 'main()' | grep -v main
}

doc="
# Repo Maintenance Functions

## Usage: ./make <function> [args]

## Functions:
$(funcs)

$(aliases)
"

sh() {
    echo -e "Running: \x1b[32m$*\x1b[0m"
    eval "$@"
}

exit_help() {
    echo -e "$doc"
    exit 1
}

function tests {
    test -z "$1" && pytest -xs tests
    test -n "$1" && pytest "$@"
}

function docs_regen {
    sh doc pre_process \
        --patch_mkdocs_filewatch_ign_lp \
        --gen_theme_link \
        --gen_last_modify_date \
        --gen_change_log \
        --gen_change_log_versioning_stanza=semver \
        --gen_change_log \
        --gen_credits_page \
        --gen_auto_docs \
        --lit_prog_evaluation=md \
        --lit_prog_evaluation_timeout=5 \
        --lit_prog_on_err_keep_running=false || exit 1 # fail build on error

}

function docs {
    sh docs_regen
    sh mkdocs build
}

function docs_serve {
    sh docs_regen
    sh mkdocs serve &
    sleep 1
    # `doc pp -h` reg. what this does (lp eval on file change):
    sh doc pp --lpem=true --lpe=md
}

## Function Aliases:
ds() { docs_serve "$@"; }
t() { tests "$@"; }

main() {
    test -z "$1" && exit_help
    test "$1" == "-h" && exit_help
    func="$1"
    shift
    echo foo
    $func "$@"
}

main "$@"
