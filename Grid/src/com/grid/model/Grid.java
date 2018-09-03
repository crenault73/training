package com.grid.model;

public class Grid extends AbstractGridModel {

	@Override
	public void next() {
		for (int i = 0; i < this.table.length; i++) {
			for (int j = 0; j < this.table[i].length; j++) {
				// this.table[i][j]++;
				if (this.table[i][j] > 5) {
					try {
						this.table[i][j - 1]++;
					} catch (Exception e) {
						// e.printStackTrace();
					}

				}
				if (this.table[i][j] > 9) {
					try {
						this.table[i][j] = 0;
						this.table[i][j + 1]++;
					} catch (Exception e) {
						// e.printStackTrace();
					}

				}

			}
		}
		notifyObserver();
	}

	@Override
	public void reset() {
		System.out.println("Reset");
		this.table = new int[10][10];
		int k = 0;
		for (int i = 0; i < this.table.length; i++) {
			for (int j = 0; j < this.table[i].length; j++) {
				this.table[i][j] = 0; // k++;
			}
		}
		notifyObserver();
	}

	@Override
	public void set(int i, int j, int val) {
		System.out.println("Set: grid(" + i + "," + j + "):" + val);
		this.table[i][j] = val;
		notifyObserver();
	}

	@Override
	public void run() {
		System.out.println("Inside : " + Thread.currentThread().getName());

	}

}