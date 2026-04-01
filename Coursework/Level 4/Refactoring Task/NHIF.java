public class NHIFSystem {

    // Global-style variables (Data)
    static String patientName = "Jaymin";
    static String policyNumber = "NHIF-B123";

    // Standalone logic (Function)
    public static double calculateClaim(double amount) {
        double coPayment = amount * 0.10;
        return amount - coPayment;
    }

    public static void main(String[] args) {
        double bill = 12000.0;
        
        // We call the function directly without 'new Patient()'
        double payout = calculateClaim(bill);
        
        System.out.println("Patient: " + patientName);
        System.out.println("NHIF Payout: " + payout + " KES");
    }
}