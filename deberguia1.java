/**
 * Hello world!
 *
 */
public class manzanas{

    private String familia;
    private int peso;

    //inicializar valores
    public manzanas(){
        System.out.println("construimos: manzanas ()");
        }

        public manzanas(String familia, int peso){ //en gramos
            this.familia = familia;
            this.peso = peso;
            }

    //setters and getters

    public void setfamilia (String familia){
        System.out.println("usando.....setfamilia (String familia ");
        this.familia = familia;

    }

    public String getfamilia (String familia){
        return this.familia;
    }

    public void setpeso (int peso){
        this.peso = peso;

    }

    public int getpeso (int peso){
        return this.peso;
    }

    public static void main(String [] args){
        System.out.println("inicio del programa");

        manzanas Objmanzanas;
        //cosntruimos objetos
        Objmanzanas = new manzanas(); //constructor vacio
        Objmanzanas.setfamilia("manzana de ecuador");

        String familiaData = Objmanzanas.getfamilia();

        System.out.println("familia" + familiaData);

        System.out.println("fin del programa");

        manzanas Objmanzanas;
        //cosntruimos objetos
        Objmanzanas = new manzanas("manzana de colombia", 15); //constructor vacio
        Objmanzanas.setfamilia("manzana de ecuador");

        String familiaData = Objmanzanas.getfamilia();

        System.out.println("familia" + familiaData);

        System.out.println("fin del programa");

        }
}
