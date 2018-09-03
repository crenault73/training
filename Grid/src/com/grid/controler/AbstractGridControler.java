package com.grid.controler;

import com.grid.model.AbstractGridModel;

public class  AbstractGridControler {

	protected AbstractGridModel grid;

	public AbstractGridControler(AbstractGridModel grid) {
		super();
		this.grid = grid;
	}

	// Retourne le modele associé
	public AbstractGridModel getGrid() {
		return grid;
	}

	// Efface
	public void reset() {
		this.grid.reset();
	}

	// Next
	public void next() {
		this.grid.next();
	}
	
//	public abstract void run();
}
