import starkbank
import sys

project = starkbank.Project(
    environment=sys.argv[1],
    id=sys.argv[2],
    private_key=sys.argv[3]
)

starkbank.user = project
