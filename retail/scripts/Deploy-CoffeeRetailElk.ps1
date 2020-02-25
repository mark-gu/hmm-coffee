param (
    [string]
    $DomainName = 'coffee-retail-elk',

    [ValidateSet('dev','uat','prd')]
    [string]
    $Environment = 'dev'
)

$ESDomainName = "$DomainName-$Environment"
aws cloudformation deploy --stack-name $ESDomainName --template-file "../templates/coffee-retail-elk.yml" --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM --parameter-overrides ESDomainName=$ESDomainName
