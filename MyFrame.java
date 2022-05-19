import java.awt.*;
import javax.swing.*;

public class MyFrame extends JFrame{// implements ActionListener{
    JButton button; //global button
    JLabel label;
    public static Pontos pontos[] = new Pontos[32];
    public String doArquivo = "";
    public String []dividir = new String[3];
    public int x = 0;
    public int y = 0;
    
    MyFrame(){
        //JButton = a button that performs an action when clicked on
      /* button = new JButton(); //instanciate new button
       button.setBounds(200, 100, 100, 50); //set bounds of it
       button.addActionListener(this); //listener to the action method below
       button.setText("Hello"); //you know
       button.setFocusable(false); //take away the anoying bar around the text
       this.add(button); //need to add to jframe
        //button,setHorizontalTextPosition(JButton.CENTER); etc
        button.setBorder(BorderFactory.createEtchedBorder()); //modifies border
        */
        // button.addActionListener(e -> System.out.println("hi")); can do lambda instruction  
        //JFrame frame = new JFrame();  //creates a frame
        this.setTitle("Estação de Metro Paris"); //sets the title of the frame 
        this.setSize(720,720); //sets the x and y dimension for the frame
        this.setVisible(true); //Makes the frame visible
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //Exit out of the application
        
        label = new JLabel();

        ImageIcon image = new ImageIcon("Metro_Logo.jpg"); //create an ImageIcon
        this.setIconImage(image.getImage()); //change icon of the frame
        this.getContentPane().setBackground(new Color(0xFFFFFF)); //change background color, can also use(255,255,255)
        
        label.setIcon(image);
        label.setBounds(150, 250, 150, 150);
        label.setVisible(false);
        this.add(label);
    }

    /*@Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource()==button){
            System.out.println("Hi");
            button.setEnabled(false); //disables a button
            label.setVisible(true);
        }*/
        //Fazer a leitura dos pontos
        
        public void leitura(){
        Arq.openRead("Coordenadas.txt");
        for (int j = 0; j < 32; j++) {
            doArquivo = Arq.readLine();
            dividir = doArquivo.split(",");
            x = Integer.parseInt(dividir[1]);
            y = Integer.parseInt(dividir[2]);
            pontos[j] = new Pontos(dividir[0],x,y);
        }
        Arq.close();
        }
 
        public void paint(Graphics g){
         Graphics2D g2D = (Graphics2D) g;
         g2D.setPaint(Color.yellow);
         g2D.fillOval(50,50,10,10);
         for(int i = 0; i < 32; i++){
         g2D.fillOval(pontos[i].x,pontos[i].y,10,10);
        }

        }
        
    }
