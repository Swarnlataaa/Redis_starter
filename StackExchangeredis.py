using StackExchange.Redis;
using System;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            // Connect to Redis
            ConnectionMultiplexer redis = ConnectionMultiplexer.Connect("localhost:6379");

            // Get the default database
            IDatabase db = redis.GetDatabase();

            // Perform Redis operations
            db.StringSet("key", "value");
            string value = db.StringGet("key");
            Console.WriteLine(value);
        }
        catch (RedisConnectionException e)
        {
            Console.WriteLine("Redis connection error: " + e.Message);
        }
        catch (Exception e)
        {
            Console.WriteLine("An error occurred: " + e.Message);
        }
    }
}
