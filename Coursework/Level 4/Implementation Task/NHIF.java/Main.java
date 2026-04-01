public class Main {
    public static void main(String[] args) {
        Patient p1 = new Patient("Jaymin", "NHIF-B123");
        
        double billAmount = 12000.0;
        double nhifCovers = p1.calculateClaim(billAmount);
        
        System.out.println("Processing claim for: " + p1.getName());
        System.out.println("NHIF will pay: " + nhifCovers + " KES");
    }
}