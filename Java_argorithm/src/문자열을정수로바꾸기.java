import java.util.ArrayList;

public class 문자열을정수로바꾸기 {




    public static void main(String[] args) {

        Main.print();

        ArrayList<Integer> list1 = new ArrayList<Integer>();
        list1.add(5);
        list1.add(4);
        list1.add(3);
        list1.add(2);
        list1.add(1);
        list1.add(0);

        ArrayList<Integer> list2 = new ArrayList<>(list1.subList(1,4));


        for (int i = 1; list2.size() - i >= 0; i--) {
            if (list1.contains(list2.get(i))) {
                list2.remove(i);
            }

        }

        print(list1,list2);

    }

    static void print(ArrayList list1, ArrayList list2){
        System.out.println("list1:" + list1);
        System.out.println("list2 = " + list2);
        System.out.println();
    }
}
