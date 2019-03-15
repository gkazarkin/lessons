package Lesson_Ex;

import lib.CoreTestCase;
import lib.ui.ArticlePageObject;
import lib.ui.SearchPageObject;
import org.junit.Test;

public class Ex8 extends CoreTestCase {

    @Test
    public void testCheckJavaText() {
        SearchPageObject SearchPageObject = new SearchPageObject(driver);
        SearchPageObject.initSearchInput();
        SearchPageObject.typeSearchLine("Java");
        SearchPageObject.waitForSearchResult("Object-oriented programming language");
        SearchPageObject.waitForSearchResult("Island of Indonesia");
        SearchPageObject.waitForSearchResult("JavaScript");
        SearchPageObject.waitForCancelButtonToAppear();
        SearchPageObject.clickCancelSearch();
        //Тут падает почему-то, не закрывает на кнопку, но падение в месте метода waitForCancelButtonToDisappear,
        // "Search cancel button 'X' is still present", хотя код вроде в порядке
        SearchPageObject.waitForCancelButtonToDisappear();
        SearchPageObject.assertThereIsNoResultOfSearch();
    }

    @Test
    public void testSaveArticlesToMyListAndDeleteOne() {
        SearchPageObject SearchPageObject = new SearchPageObject(driver);
        SearchPageObject.initSearchInput();
        SearchPageObject.typeSearchLine("Java");
        SearchPageObject.clickByArticleWithSubstring("Object-oriented programming language");
        ArticlePageObject ArticlePageObject = new ArticlePageObject(driver);
        ArticlePageObject.waitForTitleElement();
        String article_title = ArticlePageObject.getArticleTitle();
        String name_of_folder = "Learning programming";
        //Тут у меня какой-то баг, не находит локатор "//android.widget.ImageView[@content-desk='More options']"
        //хотя код вроде в порядке
        ArticlePageObject.addArticleToMyList(name_of_folder);
        ArticlePageObject.closeArticle();
        //Добавление 2ой статьи
        SearchPageObject.initSearchInput();
        SearchPageObject.typeSearchLine("Appius");
        SearchPageObject.clickByArticleWithSubstring("Roman politician");
        ArticlePageObject.waitForTitleElement();
        String article_title2 = ArticlePageObject.getArticleTitle();
        String name_of_folder2 = "Appius Claudius Caecus";
        ArticlePageObject.addArticleToMyList(name_of_folder2);
        ArticlePageObject.closeArticle();
        //Переход в избранное
        ArticlePageObject.clickOptionMenuButton(name_of_folder);
        String article_title3 = ArticlePageObject.getArticleTitle();
        assertEquals("Unexpected title not about 'Java language'", article_title2, "Java (programming language)" );
        assertEquals("Unexpected title not about 'Appius'", article_title3, "Appius Claudius Caecus" );
    }

    //Этот тест отрабатывает нормально
    @Test
    public void testCompareArticleTitle() {
        SearchPageObject SearchPageObject = new SearchPageObject(driver);
        SearchPageObject.initSearchInput();
        SearchPageObject.typeSearchLine("Java");
        SearchPageObject.clickByArticleWithSubstring("Object-oriented programming language");
        ArticlePageObject ArticlePageObject = new ArticlePageObject(driver);
        ArticlePageObject.waitForTitleElementFast();
    }
}
