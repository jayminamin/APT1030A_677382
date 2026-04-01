public class Patient {
    private String name;
    private String policyNumber;
    private final double CO_PAY_RATE = 0.10;

    public Patient(String name, String policyNumber) {
        this.name = name;
        this.policyNumber = policyNumber;
    }

    public double calculateClaim(double amount) {
        double coPayment = amount * CO_PAY_RATE;
        return amount - coPayment;
    }

    public String getName() { return name; }
}