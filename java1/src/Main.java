public class Main {
    public static void main(String[] args) {
        StringBuilder outputBuffer = new StringBuilder();
        // 1-10
        outputBuffer.append("1 5 6");
        // 10-100
        for (int waiter = 10; waiter < 100; waiter++){
            if (((waiter * (waiter - 1)) % 100) == 0){
                outputBuffer.append(" ");
                outputBuffer.append(waiter);
            }
        }
        // 100-1000
        for (int waiter = 100; waiter < 1000; waiter++){
            if (((waiter * (waiter - 1)) % 1000) == 0){
                outputBuffer.append(" ");
                outputBuffer.append(waiter);
            }
        }
        // 1000-10000
        for (int waiter = 1000; waiter < 10000; waiter++){
            if (((waiter * (waiter - 1)) % 10000) == 0){
                outputBuffer.append(" ");
                outputBuffer.append(waiter);
            }
        }
        System.out.println(outputBuffer);
    }
}