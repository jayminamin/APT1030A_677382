import java.util.Scanner;

public class HospitalSystem {
    public static void checkAccess(String role) throws Exception {
        if (!role.equals("Doctor")) {
            throw new Exception("Unauthorized Access: Role must be Doctor.");
        }
        System.out.println("Access Granted.");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter role: ");
        String userRole = scanner.nextLine();

        try {
            checkAccess(userRole);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}