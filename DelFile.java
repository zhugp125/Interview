import java.io.File;
import java.io.FilenameFilter;

public class DelFile {
    static void deleteFile(File file) {
        if (!file.exists()) {
            return ;
        }

        if (file.isDirectory()) {
            File[] files = file.listFiles();
            for (File f : files) {
                deleteFile(f);
            }
        }
        file.delete();
    }

    public static void main(String[] args) {
        deleteFile(new File("test"));
    }
}
