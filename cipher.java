import java.util.Scanner;

public class cipher {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the plaintext: ");
        String plaintext = scanner.nextLine();

        System.out.print("Enter the key: ");
        String key = scanner.nextLine();

        String ciphertext = encrypt(plaintext, key);
        System.out.println("Ciphertext: " + ciphertext);

        String decryptedText = decrypt(ciphertext, key);
        System.out.println("Decrypted Text: " + decryptedText);

        scanner.close();
    }

    public static String encrypt(String plaintext, String key) {
        StringBuilder ciphertext = new StringBuilder();

        String upperCasePlaintext = plaintext.toUpperCase();
        String upperCaseKey = key.toUpperCase();

        for (int i = 0; i < upperCasePlaintext.length(); i++) {
            char plainChar = upperCasePlaintext.charAt(i);
            char keyChar = upperCaseKey.charAt(i % upperCaseKey.length());

            if (Character.isLetter(plainChar)) {
                char encryptedChar = (char) ((plainChar + keyChar - 2 * 'A') % 26 + 'A');
                ciphertext.append(encryptedChar);
            } else {
                ciphertext.append(plainChar);
            }
        }

        return ciphertext.toString();
    }

    public static String decrypt(String ciphertext, String key) {
        StringBuilder decryptedText = new StringBuilder();
        String upperCaseCiphertext = ciphertext.toUpperCase();
        String upperCaseKey = key.toUpperCase();

        for (int i = 0; i < upperCaseCiphertext.length(); i++) {
            char cipherChar = upperCaseCiphertext.charAt(i);
            char keyChar = upperCaseKey.charAt(i % upperCaseKey.length());

            if (Character.isLetter(cipherChar)) {
                int decryptedCharValue = (cipherChar - keyChar + 26) % 26;
                char decryptedChar = (char) (decryptedCharValue + 'A');
                decryptedText.append(decryptedChar);
            } else {
                decryptedText.append(cipherChar);
            }
        }

        return decryptedText.toString();
    }
}
