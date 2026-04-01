import java.util.Scanner;

public class SaccoRecord {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter Member Name: ");
        String memberName = scanner.nextLine();

        System.out.print("Enter Member ID: ");
        int memberId = scanner.nextInt();

        double[] contributions = new double[6];
        double totalSavings = 0; 
        System.out.println("Enter contributions for 6 months:");
        for (int i = 0; i < 6; i++) {
            System.out.print("Month " + (i + 1) + ": ");
            contributions[i] = scanner.nextDouble();
            totalSavings += contributions[i];
        }

        System.out.println("\n--- SACCO Statement ---");
        System.out.println("Member: " + memberName + " (ID: " + memberId + ")");
        System.out.println("Total Savings: KES " + totalSavings);
        
        scanner.close();
    }
}