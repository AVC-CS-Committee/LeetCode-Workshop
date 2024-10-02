package LCProblem3Easy; //Do not change the package name

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class LCP3E { // Do not change the class name

    static int listNum;
    static List<Integer> listNumbers = new ArrayList<>();

    public static void createList() {
        System.out.print("Enter count in list: ");
        Scanner scnr = new Scanner(System.in);
        listNum = scnr.nextInt();
        System.out.println();
        for (int i = 0; i < listNum; i++) {
            System.out.println("Enter a " + i + "st" + "number");
            listNumbers.add(scnr.nextInt());
        }
    }

    public static void main(String[] args) {

        createList(); 

    }
}