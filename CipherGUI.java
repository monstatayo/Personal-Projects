
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JPanel;

public class CipherGUI extends JFrame {
    private JTextField textField, keyField;
    private JTextArea outputArea;

    public CipherGUI() {
        setLayout(new BorderLayout());

        JPanel inputPanel = new JPanel();
        inputPanel.setLayout(new GridLayout(4, 2));

        inputPanel.add(new JLabel("Text:"));
        textField = new JTextField();
        inputPanel.add(textField);

        inputPanel.add(new JLabel("Key:"));
        keyField = new JTextField();
        inputPanel.add(keyField);

        JButton encryptButton = new JButton("Encrypt");
        inputPanel.add(encryptButton);

        JButton decryptButton = new JButton("Decrypt");
        inputPanel.add(decryptButton);

        JButton infoButton = new JButton("Info");
        inputPanel.add(infoButton);

        infoButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFrame infoFrame = new JFrame("Vigenere Cipher Info");
                infoFrame.setSize(400, 400);
                infoFrame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
                
                JPanel infoPanel = new JPanel();
                infoPanel.setLayout(new BorderLayout());
                
                JTextArea infoText = new JTextArea();
                infoText.setText("The Vigenere Cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt and decrypt messages.\nIt is an extension of the Caesar Cipher, where each letter in the plaintext is shifted by a different amount based on the corresponding letter in the keyword.\nThe Vigenere Cipher provides stronger security compared to the Caesar Cipher, as it introduces multiple alphabetic shifts.\n\n"
                        + "The table below shows the Vigenere Square, \nwhich is used to determine the shift for each letter in the plaintext. The rows and columns represent the letters of the alphabet, and each cell contains the resulting letter after applying the shift.\n\n"
                        + "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z\n"
                        + "B C D E F G H I J K L M N O P Q R S T U V W X Y Z A\n"
                        + "C D E F G H I J K L M N O P Q R S T U V W X Y Z A B\n"
                        + "D E F G H I J K L M N O P Q R S T U V W X Y Z A B C\n"
                        + "E F G H I J K L M N O P Q R S T U V W X Y Z A B C D\n"
                        + "F G H I J K L M N O P Q R S T U V W X Y Z A B C D E\n"
                        + "G H I J K L M N O P Q R S T U V W X Y Z A B C D E F\n"
                        + "H I J K L M N O P Q R S T U V W X Y Z A B C D E F G\n"
                        + "I J K L M N O P Q R S T U V W X Y Z A B C D E F G H\n"
                        + "J K L M N O P Q R S T U V W X Y Z A B C D E F G H I\n"
                        + "K L M N O P Q R S T U V W X Y Z A B C D E F G H I J\n"
                        + "L M N O P Q R S T U V W X Y Z A B C D E F G H I J K\n"
                        + "M N O P Q R S T U V W X Y Z A B C D E F G H I J K L\n"
                        + "N O P Q R S T U V W X Y Z A B C D E F G H I J K L M\n"
                        + "O P Q R S T U V W X Y Z A B C D E F G H I J K L M N\n"
                        + "P Q R S T U V W X Y Z A B C D E F G H I J K L M N O\n"
                        + "Q R S T U V W X Y Z A B C D E F G H I J K L M N O P\n"
                        + "R S T U V W X Y Z A B C D E F G H I J K L M N O P Q\n"
                        + "S T U V W X Y Z A B C D E F G H I J K L M N O P Q R\n"
                        + "T U V W X Y Z A B C D E F G H I J K L M N O P Q R S\n"
                        + "U V W X Y Z A B C D E F G H I J K L M N O P Q R S T\n"
                        + "V W X Y Z A B C D E F G H I J K L M N O P Q R S T U\n"
                        + "W X Y Z A B C D E F G H I J K L M N O P Q R S T U V\n"
                        + "X Y Z A B C D E F G H I J K L M N O P Q R S T U V W\n"
                        + "Y Z A B C D E F G H I J K L M N O P Q R S T U V W X\n"
                        + "Z A B C D E F G H I J K L M N O P Q R S T U V W X Y");
                infoText.setEditable(false);
                
                infoPanel.add(new JScrollPane(infoText), BorderLayout.CENTER);
                
                infoFrame.add(infoPanel);
                infoFrame.setVisible(true);
            }
        });

        JButton exitButton = new JButton("Exit");
        inputPanel.add(exitButton);

        exitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
            System.exit(0);
            }
        });

        add(inputPanel, BorderLayout.SOUTH);

        outputArea = new JTextArea();
        add(new JScrollPane(outputArea), BorderLayout.CENTER);

        encryptButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
            String text = textField.getText();
            String key = keyField.getText();

            String ciphertext = encrypt(text, key);
            outputArea.setText("Ciphertext: " + ciphertext);
            }
        });

        decryptButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
            String text = textField.getText();
            String key = keyField.getText();

            String decryptedText = decrypt(text, key);
            outputArea.setText("Decrypted Text: " + decryptedText);
            }
        });
        }

    public static void main(String[] args) {
        CipherGUI frame = new CipherGUI();
        frame.setTitle("Cipher GUI");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }

    // Add your encrypt and decrypt methods here


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
