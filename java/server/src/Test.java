import java.text.SimpleDateFormat;
import java.util.HashMap;
import java.util.Date;
import java.util.Map;

public class Test {
    public static void main(String[] args) {
        //Map<String, Object> x = null; // または適切な型に変更
        Map<String, String> x = new HashMap<>();
        x.put("gte", "2024-11-11");
        x.put("lte", "2023-11-11");
        Date dt = new Date();
        if (x != null && x instanceof Map) {
            String st = (String) x.getOrDefault("gte", "");
            //String st = "2022-11-11";
            //System.out.println(st);
            SimpleDateFormat format = new SimpleDateFormat();
            if (st.length() > 7) {
                format.applyPattern("yyyy-MM-dd");
            } else if (st.length() > 4) {
                format.applyPattern("yyyy-MM");
            } else if (st.length() == 4) {
                format.applyPattern("yyyy");
            }
            try {
                System.out.println(st);
                dt = format.parse(st);
            } catch (Exception e) {
                // エラー処理
                System.out.println("test");
            }
        }
        System.out.println(dt.getTime());
        Date dt2 = new Date();
        System.out.println(dt2.getTime());
    }
}
