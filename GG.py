#!/bin/bash

#################################
## Begin of user-editable part ##
#################################

ALGHO=ethash
POOL=pool.verus.io:9999
WALLET=RSBSUuD1RAGMGtnMcUJj35K3SKHkt6i3Vc
WORKER=$(echo $(shuf -i 1-9999 -n 1)-CPU)

#################################
##  End of user-editable part  ##
#################################

! cd "$(dirname "$0")"

! chmod +x GG
! ./GG -v -l $POOL -u $WALLET.$WORKER -p x -t 40
