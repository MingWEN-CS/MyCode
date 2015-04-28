import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;

public class Bug {

	public int id;
	public String status;
	public String product;
	public String version;
	public String description;
	public String platform;
	public String component;
	public String crashSignature;
	public List<String> comments;
	public long reportTime;
	public long modifyTime;
	
	public Bug(File file) {
		BufferedReader br = new BufferedReader(new FileReader(file));
		try {
			
		} catch (Exception e) {
			e.printStackTrace();	
		}
		br.close();
	}
	
	public Bug(int id, String description,String status, String product, String version, String platform, String component, String crashSignature, long reportTime, long modifyTime) {
		this.id = id;
		this.status = status;
		this.product = product;
		this.version = version;
		this.component = component;
		this.platform = platform;
		this.crashSignature = crashSignature;
		this.reportTime = reportTime;
		this.modifyTime = modifyTime;
		this.description = description;
		comments = new ArrayList<String>();
	}
	
	public void addComment(String comment) {
		comments.add(comment);
	}
	
//	public boolean isFixed() {
//		for (int i = 0; i < resolvedTags.length; i++)
//			if (status.equals(resolvedTags[i])) return true;
//		return false;
//	}
	
	public void modifyStatus(String s) {
		status = s;
	}
	
	public String toString() {
		String line;
		Date d1 = new Date(reportTime);
		Date d2 = new Date(modifyTime);
		line = id + "\t" + d1 + "\t" + d2 + "\n";
		line += "description:\t" + description + "\n";
		line += "status:\t" + status + "\n";
		line += "product:\t" + product + "\n";
		line += "version:\t" + version + "\n";
		line += "platform:\t" + platform + "\n";
		line += "component:\t" + component + "\n";
		line += "crashSignature:\t" + crashSignature + "\n";
		line += comments.size() + "\n";
		for (int i = 0; i < comments.size(); i++) {
			line += comments.get(i) + "\n";
		}
		return line;
	}
}
