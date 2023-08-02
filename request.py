import starkbank
from cpf_generator import CPF
from names_generator import generate_name
from random import randint

def do_transfer():
    starkbank.transfer.create([
        starkbank.Transfer(
            amount=randint(1000, 9999),
            tax_id=CPF.generate(),
            name=generate_name(style='capital'),
            bank_code="90400888",
            branch_code=str(randint(1000, 9999)),
            account_number=str(randint(10000, 99999)),
            tags=['jcfpchallenge']
        )
    ])

def do_search():
    return starkbank.transfer.query(
        limit=2,
        tags=['jcfpchallenge']
    )
