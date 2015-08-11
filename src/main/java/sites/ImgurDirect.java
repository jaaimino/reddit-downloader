/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sites;

import sites.manager.Site;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author Jacob
 */
public class ImgurDirect implements Site {

    Pattern p = Pattern.compile(".*?\\:\\/\\/i\\.imgur\\.com.*?");
    
    @Override
    public boolean fitsURLPattern(String url) {
        Matcher m = p.matcher(url);
        return m.matches();
    }

    @Override
    public List<String> findImages(String url) {
        List<String> urls = new ArrayList<>();
        urls.add(url);
        return urls;
    }

    @Override
    public String toString() {
        return "Imgur Site Instance";
    }

}