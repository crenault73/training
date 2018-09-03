package com.grid.view;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.HeadlessException;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

import com.grid.controler.AbstractGridControler;
import com.grid.model.AbstractGridModel;
import com.grid.observer.GridObserver;

public class GridView extends JFrame implements GridObserver {
	private JPanel container = new JPanel();
	private AbstractGridControler controler;
	private Dimension dim2 = new Dimension(50, 31);

	private JLabel tableDisplay = new JLabel();
	private GridDisplay gd = new GridDisplay();

	@Override
	public void update(AbstractGridModel grid) {
		// TODO Auto-generated method stub
		tableDisplay.setText("" + grid.table[0][0]);
		gd.setGridDisplay(grid.table);
		gd.repaint();
	}

	public GridView(AbstractGridControler controler) throws HeadlessException {
		super();
		gd.setGridDisplay(controler.getGrid().table);
		// gd.addMouseListener(new GridDisplayListener());
		this.setTitle("Grid");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLocationRelativeTo(null);
		this.setResizable(true);
		initComposant();
		this.controler = controler;
		this.setContentPane(container);
		this.pack();
		this.setVisible(true);
	}

	private void initComposant() {
		container.setLayout(new BorderLayout());

		Font police = new Font("Arial", Font.PLAIN, 20);
		gd.setFont(police);

		gd.setPreferredSize(new Dimension(400, 400));
		gd.setBorder(BorderFactory.createLineBorder(Color.BLUE, 2));

		JPanel controlPanel = new JPanel();
		// controlPanel.setPreferredSize(new Dimension(55, 225));
		controlPanel.setPreferredSize(new Dimension(400, 50));
		controlPanel.setBorder(BorderFactory.createLineBorder(Color.BLUE, 2));

		JButton resetButton = new JButton("Reset");
		resetButton.setForeground(Color.red);
		resetButton.addActionListener(new ResetListener());
		resetButton.setPreferredSize(dim2);
		resetButton.setBorder(BorderFactory.createLineBorder(Color.BLUE, 2));
		controlPanel.add(resetButton);

		JButton NextButton = new JButton("Next");
		NextButton.setForeground(Color.blue);
		NextButton.addActionListener(new NextListener());
		NextButton.setPreferredSize(dim2);
		NextButton.setBorder(BorderFactory.createLineBorder(Color.BLUE, 2));
		controlPanel.add(NextButton);

		container.add(controlPanel, BorderLayout.NORTH);
		container.add(gd, BorderLayout.CENTER);
		// container.add(tableDisplay, BorderLayout.SOUTH);

		// JButton button = new JButton("Button 2 (CENTER)");
		// button.setPreferredSize(new Dimension(200, 100));
		//
		// container.add(button, BorderLayout.CENTER);
		//
		// System.out.println("Layout:"+container.getLayout());

	}

	class NextListener implements ActionListener {
		public void actionPerformed(ActionEvent arg0) {
			controler.next();
		}
	}

	class ResetListener implements ActionListener {
		public void actionPerformed(ActionEvent arg0) {
			controler.reset();
		}
	}

	class GridDisplay extends JPanel {

		private int[][] gridDisplay;// = new int[10][10];

		void setGridDisplay(int[][] gridDisplay) {
			this.gridDisplay = gridDisplay;
		}

		public GridDisplay() {
			this.addMouseListener(new GridDisplayListener());
		}

		@Override
		public void paintComponent(Graphics g) {
			super.paintComponent(g);
			drawBoard(g);
			// System.out.println(b.toString());
		}

		public void drawBoard(Graphics g) {
			// System.out.println( "gridDisplay[0][2]="+gridDisplay[0][2]);
			int w = this.getWidth();
			int h = this.getHeight();
			FontMetrics fm = this.getFontMetrics(this.getFont());
			// System.out.println("Width:" + w + " Height:" + h + " Font: " +
			// fm);
			g.setColor(Color.black);
			try {
				System.out.println("" + "" + gridDisplay[0][0]);
			} catch (Exception e) {
				e.printStackTrace();
			}

			int boxWidth = w / gridDisplay.length;
			int boxHeight = h / gridDisplay[0].length;
			for (int i = 0; i < gridDisplay.length; i++) {
				for (int j = 0; j < gridDisplay[0].length; j++) {
					g.drawRect(j * boxWidth, i * boxHeight, boxWidth, boxHeight);

					// if (i == 1 && j == 0)
					g.drawString("" + gridDisplay[i][j],
							(j * boxWidth) - fm.stringWidth("" + gridDisplay[i][j]) / 2 + boxWidth / 2,
							(i * boxHeight) + fm.getHeight() / 2 + boxHeight / 2);
				}
			}
		}

		class GridDisplayListener implements MouseListener {

			public void mousePressed(MouseEvent e) {
				int w = GridDisplay.this.getWidth();
				int h = GridDisplay.this.getHeight();
				int boxWidth = w / GridDisplay.this.gridDisplay.length;
				int boxHeight = h / GridDisplay.this.gridDisplay[0].length;
				int j = e.getX()/boxWidth;
				int i = e.getY()/boxHeight;
				GridView.this.controler.getGrid().set(i, j, 7);
				System.out.println("Width:" + w + " Height:" + h+"grid(i):" + i + " grid(j):" + j);
				System.out.println("Mouse pressed; # of clicks: " + e.getClickCount() + " Point: " + e.getPoint());
			}

			public void mouseReleased(MouseEvent e) {
//				System.out.println("Mouse released; # of clicks: " + e.getClickCount());
			}

			public void mouseEntered(MouseEvent e) {
//				System.out.println("Mouse entered");
			}

			public void mouseExited(MouseEvent e) {
//				System.out.println("Mouse exited");
			}

			public void mouseClicked(MouseEvent e) {
				System.out.println("Mouse clicked (# of clicks: " + e.getClickCount() + ")");
			}

		}
	}

}
