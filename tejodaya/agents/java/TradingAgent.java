package tejodaya.agents;

public class TradingAgent {
    public static void main(String[] args) {
        if (args.length > 0) {
            String task = String.join(" ", args).toLowerCase();
            System.out.println("Trading Agent (Java) processing task: " + task);

            if (task.contains("analyze") || task.contains("trend")) {
                System.out.println(performTechnicalAnalysis());
            } else if (task.contains("risk")) {
                System.out.println("Calculated Risk Reward Ratio: 1:2.5. Recommended Stop Loss at 1.1200.");
            } else {
                System.out.println("Market status: Bullish. Volatility: Medium.");
            }
        } else {
            System.out.println("No task provided to Trading Agent.");
        }
    }

    private static String performTechnicalAnalysis() {
        // Simulated TA logic
        double rsi = 45.5;
        double sma20 = 1.1250;
        double sma50 = 1.1200;
        String trend = (sma20 > sma50) ? "UPTREND" : "DOWNTREND";
        return "TA Results: RSI=" + rsi + ", Trend=" + trend + " (SMA20 > SMA50).";
    }
}
