BASE="$HOME"
export PATH="$BASE/.anyenv/bin:$PATH"
eval "$(anyenv init -)"

for D in `\ls $BASE/.anyenv/envs`; do
    export PATH="$BASE/.anyenv/envs/$D/shims:$PATH"
done