import java.util.ArrayList;

public class arraylistRemove {

    public static void main(String[] args) {

        ArrayList<Integer> list1 = new ArrayList<Integer>();
        list1.add(5);
        list1.add(4);
        list1.add(3);
        list1.add(2);
        list1.add(1);
        list1.add(0);

        ArrayList<Integer> list2 = new ArrayList<>(list1.subList(1,4));

        print(list1,list2);

//        for (int i =  list1.size() - 1; i >= 0; i--) {
//
//            System.out.println("i = " + i);
//            System.out.println();
//
//            if (list2.contains(list1.get(i))) {
//                list1.remove(i);
//            }
//
//        }

        for (int i = 0;  i < list1.size(); i++) {
            System.out.println("i = " + i);
            System.out.println();
            if (list2.contains(list1.get(i))) {
                list1.remove(i);
                i -= 1;
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
