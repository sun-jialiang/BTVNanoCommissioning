#!/usr/bin/env bash

json_tag="${1:-CE}"

python runner.py \
 --wf DY_sfl \
 --json /data/dust/user/sunjiali/BTVNanoCommissioning/metadata/Prompt25/data_Prompt25_2025_DY_sfl_${json_tag}.json \
 --overwrite \
 --isSyst all \
 --campaign Winter25 \
 --year 2025 \
 --workers 1 \
 --executor futures \
 --skipbadfiles \
 --skip-structure-validation \
 --max 1 \
 --limit 1 \
 --voms /afs/desy.de/user/s/sunjiali/x509up_u56078
#  --scaleout 150