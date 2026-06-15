package jarvis.agents;

public class TradingAgent {
    public static void main(String[] args) {
        if (args.length > 0) {
            String task = String.join(" ", args);
            System.out.println("Trading Agent (Java) processing task: " + task);
            if (task.contains("market")) {
                System.out.println("Monitoring market trends...");
            } else if (task.contains("trade")) {
                System.out.println("Executing technical analysis...");
            }
        } else {
            System.out.println("No task provided to Trading Agent.");
        }
    }
}
