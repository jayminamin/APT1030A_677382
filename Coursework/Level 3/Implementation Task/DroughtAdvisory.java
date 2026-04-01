import java.util.Scanner;

public class DroughtSwitch {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter rainfall (mm): ");
        double rain = input.nextDouble();
        System.out.print("Enter temperature (C): ");
        double temp = input.nextDouble();

        // Step 1: Categorize the input
        String status;
        if (rain < 200) {
            status = "LOW_RAIN";
        } else if (temp > 30) {
            status = "HIGH_TEMP";
        } else {
            status = "NORMAL";
        }

        // Step 2: Use Switch to handle the categories
        switch (status) {
            case "LOW_RAIN":
                System.out.println("Irrigation Required");
                break;
            case "HIGH_TEMP":
                System.out.println("Monitor Soil");
                break;
            case "NORMAL":
                System.out.println("Normal Conditions");
                break;
            default:
                System.out.println("Error in logic");
        }
    }
}