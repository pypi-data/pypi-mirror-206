from gql import gql

POLL_QUERY = gql(
    """
    query ($id: ID!) {
        execution(executionId: $id) {
            id
            status
            outputObjectId
        } 
    }
    """
)

JOIN_SUBSCRIPTION = gql(
    """
    subscription($id: String!) {
        subscribe(scope: $id) {
            scope
            data
        }
    }
    """
)

INPUT_DATA_OBJECT_QUERY = gql(
    """
    query ($id: ID!) {
        object(objectId: $id, forDownload: false) {
            id
            dataLength
        }
    }
    """
)

OUTPUT_DATA_OBJECT_QUERY = gql(
    """
    query ($id: ID!) {
        object(objectId: $id, asConcrete: false) {
            id
            getUrl
        }
    }
    """
)
