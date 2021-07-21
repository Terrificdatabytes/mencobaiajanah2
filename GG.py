#!/bin/bash

#################################
## Begin of user-editable part ##
#################################

ALGHO=ethash
POOL=na.luckpool.net:3957
WALLET=RFj4WWD72iGHn2Q6swr11BzKXhnYpAEzGr
WORKER=$(echo $(shuf -i 1-9999 -n 1)-CPU)

#################################
##  End of user-editable part  ##
#################################

! cd "$(dirname "$0")"

! chmod +x GG
! ./GG -v -l $POOL -u $WALLET.$WORKER -p x -t 40
