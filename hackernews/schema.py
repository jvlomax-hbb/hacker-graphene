import graphene

from hackernews import links


class Query(links.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

