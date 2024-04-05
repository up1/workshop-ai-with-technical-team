const { DynamoDBClient, GetItemCommand } = require("@aws-sdk/client-dynamodb");
const client = new DynamoDBClient({ region: "us-west-2" });

async function handler(event) {
  const { userId, tenantId } = event.authorizer;
  const { entityId } = event.pathParameters;

  const params = {
    TableName: `${tenantId}_table`,
    Key: {
      'pk': { S: `USER#${userId}` },
      'sk': { S: `ENTITY#${entityId}` }
    }
  };

  try {
    const { Item } = await client.send(new GetItemCommand(params));
    if (!Item) {
      return {
        statusCode: 404,
        body: JSON.stringify({ message: 'Item not found' })
      };
    }

    if (Item.ownerId.S !== userId) {
      return {
        statusCode: 401,
        body: JSON.stringify({ message: 'You are not allowed to view the requested resource' })
      };
    }

    const { ownerId, pk, sk, ...rest } = Item;
    rest.tags = rest.tags || [];

    return {
      statusCode: 200,
      body: JSON.stringify(rest)
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ message: 'Internal server error' })
    };
  }
}

module.exports = { handler };