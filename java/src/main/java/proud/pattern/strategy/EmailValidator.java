package proud.pattern.strategy;

public class EmailValidator {

  ValidationStrategy strategy;

  public EmailValidator(ValidationStrategy strategy) {
    this.strategy = strategy;
  }

  public boolean isValidAddress(String emailAddress) {
    return this.strategy.isValidAddress(emailAddress);
  }

  public static void main(String[] args) {
    String address = "inv@lid@example.com";
    RegexValidation regexValidation = new RegexValidation();
    InetAddressValidation inetAddressValidation = new InetAddressValidation();
    EmailValidator validator1 = new EmailValidator(regexValidation);
    EmailValidator validator2 = new EmailValidator(inetAddressValidation);
    System.out.println(validator1.isValidAddress(address));
    System.out.println(validator2.isValidAddress(address));
  }

}
