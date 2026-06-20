import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.SUPABASE_URL as string;
const supabaseKey = import.meta.env.SUPABASE_KEY as string;

if (!supabaseUrl || !supabaseKey) {
    console.error("Could not find supabase url and supabase key in .env!");
}
export const supabase = createClient(supabaseUrl, supabaseKey);