package LCProblem2Easy; //Do not change the package name

public class LCP2E { // Do not change the class name
    public static void main(String[] args) {
        int sum = 0;
        int[] arr = {100, 200, 300, 400};
        
        for (int i = 0; i < arr.length; i++){
            if (arr[i] > 0){
                sum += arr[i];
            };
        };
        System.out.println(sum);
    }
}