package com.grid.observer;

public interface Observable {

	public void addObserver(GridObserver obs);

	public void removeObserver();

	public void notifyObserver();

}