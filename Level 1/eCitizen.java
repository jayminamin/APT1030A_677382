import java.util.Scanner;

public class eCitizenLogin {
    public static void main(String[] args) {
        String validUser = "adminKE";
        String validPass = "254Secure";

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter Username: ");
        String userInput = scanner.nextLine();

        System.out.print("Enter Password: ");
        String passInput = scanner.nextLine();

        if (userInput.equals(validUser) && passInput.equals(validPass)) {
            System.out.println("Access Granted");
        } else {
            System.out.println("Invalid Credentials");
        }
        
        scanner.close();
    }
}