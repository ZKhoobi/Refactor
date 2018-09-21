public class B{
    String data;
    public B(){
        data = "salam";
    }
    private int add(int i, int j){
        i = i + j;
        return i;
    }
}
//......................................................
class A{
    String a_data;
    public void print(B b){
        a_data = "hhh";
        String m_data = "fgfg";
        b.add(1, 2);
        system.out.print(b.data);
        b.add(3, 4);
    }
    public void test(B b){
        int i = 6;
    }
}