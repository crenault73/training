package com.grid.model;

import java.util.ArrayList;

import com.grid.observer.GridObserver;
import com.grid.observer.Observable;

public abstract class AbstractGridModel implements Observable, Runnable {

	private ArrayList<GridObserver> listObserver = new ArrayList<GridObserver>();
	public int[][]table = new int[10][10];

	public AbstractGridModel(){
		this.reset();
	}
	
	// Efface
	public abstract void reset();

	// Calcul l'etape suivante
	public abstract void next();
	
	// Set Set: grid(i,j)= val;
	public abstract void set(int i, int j, int val);

	// Implémentation du pattern observer
	public void addObserver(GridObserver obs) {
		this.listObserver.add(obs);
	}
	
	public void removeObserver() {
		listObserver = new ArrayList<GridObserver>();
	}

	public void notifyObserver() {
		for (GridObserver obs : listObserver)
			obs.update(this);
	}

}
