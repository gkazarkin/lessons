package lib.ui;

import io.appium.java_client.AppiumDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

public class ArticlePageObject extends MainPageObject {

    private static final String
        TITLE = "org.wikipedia:id/view_page_title_text",
        FOOTER_ELEMENT = "//*[@text='View page in browser']",
        OPTIONS_BUTTON = "//android.widget.ImageView[@content-desk='More options']",
        OPTION_MAIN_BUTTON = "//android.widget.FrameLayout[@content-desk='My lists'",
        FIRST_SAVED_ARTICLE = "//*[@text='Java (programming language)']",
        APPIUS_TITLE = "//*[@text='Appius']",
        OPTIONS_ADD_TO_MY_LIST_BUTTON = "//*[@text='Add to reading list']",
        ADD_TO_MY_LIST_OVERLAY = "org.wikipedia:id/onboarding_button",
        MY_LIST_NAME_INPUT = "org.wikipedia:id/text_input",
        MY_LIST_OK_BUTTON = "//*[@content-desk='OK'",
        CLOSE_ARTICLE_BUTTON = "//android.widget.ImageButton[@content-desk='Navigate up'";


    public ArticlePageObject(AppiumDriver driver) {
        super(driver);
    }

    public WebElement waitForTitleElement() {
        return this.waitForElementPresent(By.id(TITLE),
                "Cannot find article title on page", 15);
    }

    public WebElement waitForTitleElementFast() {
        return this.waitForElementPresent(By.id(TITLE),
                "Cannot find article title on page", 0);
    }

    public String getArticleTitle() {
        WebElement title_element = waitForTitleElement();
        return title_element.getAttribute("text");
    }

    public void swipeToFooter() {
        this.swipeUpToFindElement(By.xpath(FOOTER_ELEMENT), "Cannot find the end of article", 20);
    }

    public void addArticleToMyList(String name_of_folder) {
        this.waitForElementPresent(By.xpath(OPTIONS_BUTTON), "Cannot find button to open article options", 15);
        this.waitForElementAndClick(By.xpath(OPTIONS_BUTTON),
                "Cannot find button to open article options", 15);
        this.waitForElementAndClick(By.xpath(OPTIONS_ADD_TO_MY_LIST_BUTTON),
                "Cannot find option to add article to reading list", 5);
        this.waitForElementAndClick(By.id(ADD_TO_MY_LIST_OVERLAY),
                "Cannot find button 'GOT IT' tip overlay", 5);
                this.waitForElementAndClear(By.id(MY_LIST_NAME_INPUT),
                "Cannot find input to set name of article folder", 5);
        this.waitForElementAndSendKeys(By.id(MY_LIST_NAME_INPUT),
                name_of_folder, "Cannot put text into articles folder input", 5);
        this.waitForElementAndClick(By.xpath(MY_LIST_OK_BUTTON),
                "Cannot press 'OK' button", 5);
    }

    public void clickOptionMenuButton(String name_of_folder) {
        this.waitForElementPresent(By.xpath(OPTION_MAIN_BUTTON), "Cannot find navigation button to 'My lists'", 15);
        this.waitForElementAndClick(By.xpath(OPTION_MAIN_BUTTON),
                "Cannot click navigation button to 'My lists'", 15);
        this.waitForElementAndClick(By.xpath("//*[@text='" + name_of_folder + "']"),
                "Cannot find created folder in 'My lists'", 5);
        this.swipeElementToLeft(By.xpath(FIRST_SAVED_ARTICLE),
                "Cannot find saved article about 'Java'");
        waitForElementAndClick(By.xpath(APPIUS_TITLE), "Cannot click on 'Appius Claudius Caecus'",
                15 );
//        WebElement title_element = waitForElementPresent(
//                By.id("org.wikipedia:id/view_page_title_text"), "Cannot find text about 'Appius' to check title article",
//                15);
//        String article_title = title_element.getAttribute("text");
    }

    public void closeArticle() {
        this.waitForElementAndClick(By.xpath(CLOSE_ARTICLE_BUTTON),
                "Cannot close article or cannot find 'X' button", 5);
    }
}
