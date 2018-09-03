import com.grid.controler.AbstractGridControler;
import com.grid.controler.GridControler;
import com.grid.model.AbstractGridModel;
import com.grid.model.Grid;
import com.grid.view.GridView;

// https://openclassrooms.com/fr/courses/26832-apprenez-a-programmer-en-java/25552-mieux-structurer-son-code-le-pattern-mvc
public class MyGrid {

	public static void main(String[] args) {
		// Instanciation de notre modèle
		AbstractGridModel grid = new Grid();
		// Création du contrôleur
		AbstractGridControler controler = new GridControler(grid);
		// Création de notre fenêtre avec le grid en paramètre
		GridView gridView = new GridView(controler);
		// Ajout de la fenêtre comme observer de notre modèle
		grid.addObserver(gridView);
	}
}