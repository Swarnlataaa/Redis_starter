import redis.clients.jedis.Jedis;
import redis.clients.jedis.exceptions.JedisConnectionException;

public class RedisExample {
    public static void main(String[] args) {
        try {
            // Connect to Redis
            Jedis jedis = new Jedis("localhost", 6379);

            // Perform Redis operations
            jedis.set("key", "value");
            String value = jedis.get("key");
            System.out.println(value);
        } catch (JedisConnectionException e) {
            System.err.println("Redis connection error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}
