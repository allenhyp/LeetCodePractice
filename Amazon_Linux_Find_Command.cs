using System.Linq;
public class File {
    public string name;
    public int size;
    public string extension;
    public bool isDirectory;
    public List<File> children;
}

public abstract class Filter {
    public abstract bool apply (File file);
}

public class SizeFilter : Filter {
    public enum SizeOperator {
        LT,
        LTE,
        EQ,
        GT,
        GTE,
    };
    private int targetSize;
    private SizeOperator op;
    public SizeFilter(int targetSize, SizeOperator op) {
        this.targetSize = targetSize;
        this.op = op;
    }

    public override bool apply(File file)
    {
        switch (this.op){
            case SizeOperator.LT:
                return file.size < this.targetSize;
            case SizeOperator.LTE:
                return file.size <= this.targetSize;
            case SizeOperator.EQ:
                return file.size == this.targetSize;
            case SizeOperator.GT:
                return file.size > this.targetSize;
            case SizeOperator.GTE:
                return file.size >= this.targetSize;
        }

        return false;
    }
}

public class ExtensionFilter : Filter {
    private string extension;
    public ExtensionFilter(string extension) {
        this.extension = extension;
    }

    public override bool apply(File file)
    {
        // return file.getName().split('.')[-1].Last() == this.extension;
        return file.extension == this.extension; 
    }
}

public class FindCommand {
    public List<File> findFilesWithFilters(File directory, Filter filter) {
        if (!directory.isDirectory) {
            throw new NotADirectoryException();
        }

        List<File> output = new List<File> ();
        findFilesWithFilters(directory, filter, ref output);
        return output;
    }

    public void findFilesWithFilters(File directory, Filter filter, ref List<File> output) {
        foreach (File child in directory.children) {
            if (child.isDirectory){
                findFilesWithFilters(child, filter, ref output);
            }
            else {
                if (filter.apply(child)) {
                    output.Add(child);
                }
            }
        }
    }
}
