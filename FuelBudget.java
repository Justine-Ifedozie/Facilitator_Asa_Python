import java.util.Scanner;
public class FuelBudget {
	public static void main (String[] args) { 
		Scanner keyboardInput = new Scanner(System.in);

		int pricePerLiter = 855; //Per liter
		double result = 0;

		System.out.print("Enter your total budget for the fuel purchase: ");
		double userBudget = keyboardInput.nextInt();

		result = userBudget / pricePerLiter;

		System.out.printf("The number of liters you can purchase from the gas station with %f naira is: %.3f liters", userBudget, result);




	}

}

