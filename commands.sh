az group create -l eastus2 -n "udcaity-project2-rg"
az webapp up --sku F1 -l eastus2 -g "udcaity-project2-rg" -n "udacity-project2-app"