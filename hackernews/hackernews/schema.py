import graphene
import graphql_jwt
from links.schema import Query as LinksQuery
from links.schema import Mutation as LinksMutation
from users.schema import Mutation as UserMutation
from users.schema import Query as UsersQuery
from links.schema_relay import RelayQuery, RelayMutation


class Query(LinksQuery, UsersQuery, RelayQuery, graphene.ObjectType):
    pass


class Mutation(LinksMutation, UserMutation, RelayMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)



