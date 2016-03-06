package com.example.cruz.microbuzzapp.uifragments;

import android.support.v4.app.Fragment;
import android.view.Menu;
import android.view.MenuInflater;

import com.example.cruz.microbuzzapp.R;

/**
 * Created by Cruz on 05/03/2016.
 */
public class PantallaPeatonFragment extends Fragment {
    @Override
    public void onCreateOptionsMenu(Menu menu, MenuInflater inflater) {
        //super.onCreateOptionsMenu(menu, inflater);
        inflater.inflate(R.menu.menu_peaton,menu);
    }
}
