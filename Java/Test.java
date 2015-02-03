import java.io.File;

public class Test {
	public static void main(String[] args) {
		int id = 602225;
		File file = new File(id + ".txt");
		Bug bug = new Bug(file);
//		System.out.println("Hello World");	
	}	
}
