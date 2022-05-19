import java.awt.Color;
import java.awt.Font;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.Border;

/*
 Author: Bryan Jonathan Melo De Oliveira
 Matricula: 708688
*/
public class Main {
    public static void main(String[] args) {
        // Definir dados
        String doArquivo = "";
        String []dividir = new String[3];
        Pontos pontos[] = new Pontos[32];
        int x = 0;
        int y = 0;

        // JLabel = a GUI display area for a string of text, an image, or both
          JLabel label = new JLabel();
          label.setText("Hello World"); //set text of label
          ImageIcon image = new ImageIcon("Metro_Logo.jpg");
          Border border = BorderFactory.createLineBorder(Color.green, 3);
          label.setIcon(image);
          label.setHorizontalTextPosition(JLabel.CENTER); //set text LEFT, CENTER, RIGHT of imageicon
          label.setVerticalTextPosition(JLabel.TOP); //set text TOP, CENTER, BOTTOM of imageIcon
          label.setForeground(Color.green); //set Color text
          label.setFont(new Font("Arial", Font.BOLD, 48)); //set font type, format and size
          label.setIconTextGap(50); //set gap of the text to image
          label.setBackground(Color.blue); //set background color
          label.setOpaque(true); //display background color
          label.setBorder(border); //border of the label
          label.setVerticalAlignment(JLabel.CENTER); //set vertical position of icon+text within label
          label.setHorizontalAlignment(JLabel.CENTER); //set horizontal position of icon+text within label
          label.setBounds(0, 0, 250, 250); //set the bounds of a specific label (x,y,dimension,dimension)
          
          
          
          //JPanel = a GUI component that functions as a container to hold other components
          JPanel panel = new JPanel();
          panel.setBackground(Color.red);
          panel.setBounds(250, 250, 250, 250); //set bounds panel
         
          
          //JFrame = My frame
          MyFrame myFrame = new MyFrame(); //you can use just new MyFrame();
          myFrame.add(label);
          myFrame.add(panel);
          myFrame.setLayout(null); //so we can manually manipulate the layout
          //myFrame.pack(); //accomodate the size of everything inside the label (add all components before using this)
         
        //Fazer a leitura dos pontos
        Arq.openRead("Coordenadas.txt");
        for (int j = 0; j < 32; j++) {
            doArquivo = Arq.readLine();
            dividir = doArquivo.split(",");
            x = Integer.parseInt(dividir[1]);
            y = Integer.parseInt(dividir[2]);
            pontos[j] = new Pontos(dividir[0],x,y);
        }
        Arq.close();
        /*for (int i = 0; i < 32; i++) {
            System.out.println(pontos[i].nome + pontos[i].x + pontos[i].y);
        }*/
    }
    
}
