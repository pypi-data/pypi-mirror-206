from amazon_sagemaker_jupyter_scheduler.clients import get_sts_client, get_sagemaker_client


async def get_aws_account_id():
    get_caller_identity_response = await get_sts_client().get_caller_identity()
    return get_caller_identity_response.get("Account")


async def get_domain_id():
    list_domains_response = await get_sagemaker_client().list_domains()
    domains = list_domains_response.get("Domains")
    if domains:
        return domains[0].get("DomainId")
    return None
