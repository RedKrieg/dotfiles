alias engage="play -n -c1 synth whitenoise lowpass -1 120 lowpass -1 120 lowpass -1 120 gain +14"
function cdiff {
    [ ! -z $(which colordiff) ] && colordiff -u $@ || diff -u $@
} 
